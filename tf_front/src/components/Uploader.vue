<style>
  input[type="file"]{
    position: absolute;
    top: -500px;
  }
  div.file-listing{
    width: 200px;
  }
  span.remove-file{
    color: red;
    cursor: pointer;
    float: right;
  }
  .custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}

#circle {
    width: 42px;
    height: 42px;
    background: red;
    -moz-border-radius: 50px;
    -webkit-border-radius: 50px;
    border-radius: 50px;
}
#inner {
  width: 3%;
  margin: 0 auto;
}
#cirle-parent{
      font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 700px;
  height: 200px;
  outline: dashed 1px black;
      display: flex;
  justify-content: center;
}
</style>

<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label for="file-upload" class="custom-file-upload">Upload File
        
        <input type="file" accept="image/*" @change="onFileChanged" id="file-upload" ref="myFiles" >
  
      </label>
    </div>
 
    <div class="large-12 medium-12 small-12 cell">
      <button @click="uploadImage">Submit</button>
    </div>
    <div v-show="fileUrl">
        <img :src="fileUrl" alt="" width="400" height="400">
        <br>
        {{this.result}}
    </div>
    <div v-show="fileLoading"  id="inner">
          <div id="circle" style="background-color: coral;">
        <img src="../assets/svg-loaders/tail-spin.svg" alt="">
        {{this.explain}}
    </div>
    </div>
  
  </div>
</template>

<script>



const axios = require('axios')
const ax_instance = axios.create({
  baseURL: 'http://192.168.0.2:8080/up'
})

  export default {
  
    data(){
        return {file:'',
        fileUrl:'' ,
        result:'',
        fileLoading:false,
        explain:'Calculating....'
        }
    },
 
    methods: {


    onFileChanged (event) {
    this.file=this.$refs.myFiles.files[0]
    this.fileUrl = URL.createObjectURL(this.$refs.myFiles.files[0]);
    this.result=''
    },
   uploadImage(event) {
    let data = new FormData()
    data.append('name', 'my-picture')
    data.append('file', this.file)
    this.fileLoading=true

        ax_instance.post( '',
          data,
          {
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            
          }
        ).then((x)=>{
          console.log(x.data['result'])
          this.result=x.data['result']
          this.fileLoading=false
        })
        .catch(function(e){
          console.log(e);
        })
  
    }
    }
   }
</script>


