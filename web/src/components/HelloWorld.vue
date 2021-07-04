<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
        <div class="large-12 medium-12 small-12 cell">
        <label>File
            <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </label>
            <button v-on:click="submitFile()">Submit</button>
        </div>
    </div>
    <div>
        <ol>
            <li :key="audio" v-for="(audio, index) in audiolist" v-on:click="play(index)">
                {{audio}}
                <audio :id="index" :src="audio"></audio>
            </li>
        </ol>
    </div>
  </div>
</template>

<script>
export default {
    name: 'HelloWorld',
    props: {
        msg: String
    },
    data(){
        return {
            file: '',
            audiolist: [],
            selectedAudio: ''
        }
    },
    methods: {
      /*
        Submits the file to the server
      */
        submitFile(){
            let formData = new FormData();
            formData.append('audio-file', this.file);

            fetch("/api/audio/upload", {
                method: 'post',
                body: formData,
            })
            .then((res) => {
                console.log('SUCCESS!!');
                return res.json();
            })
            .then((data) => {
                this.audiolist.push(data);
            })
            .catch(() => {
                console.log('FAILURE!!');
            });
        },

        /*
            Handles a change on the file upload
        */
        handleFileUpload(){
            this.file = this.$refs.file.files[0];
        },

        play(index){
            var gg = document.getElementById(index);
            return gg.paused ? gg.play() : gg.pause();
        },

        selectAudio(src){
            this.selectedAudio = "/" + src;
            this.$refs.player.load();
            this.$refs.player.play();
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
