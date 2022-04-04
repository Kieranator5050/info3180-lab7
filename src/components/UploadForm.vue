<template>

    <div v-if="verified" class="alert alert-success" role="alert">
        <p>Upload Successful!</p>
    </div>
    <div v-else class="alert alert-danger" role="alert">
        <ul>
            <li v-for="error in errors" class="error"> {{ error }} </li>
        </ul>
    </div>

    <form @submit.prevent="uploadPhoto" id="uploadForm" method="post" enctype="multipart/form-data">
  		<div class="mb-3">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" name="description" rows="4" cols="50" maxlength="200"></textarea>
            <input class="form-control" type="file" id="photo" name="photo">
        </div>
        <button type="submit" name="submit" class="btn btn-primary">Upload Photo</button>
    </form>

</template>

<script>
export default {
    data() {
      return {
          csrf_token: '',
          errors: [],
          verified: false
      }        
    },
    methods : {
        uploadPhoto(){
            let self = this

            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);

                if('errors' in data){
                    self.errors = [...data.errors];
                    self.verified = false;
                } else {
                    self.errors = [];
                    self.verified = true;
                }

            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
        }        
    },
    created() {
        this.getCsrfToken();
    }
}
</script>

<style>
/* Add any component specific styles here */
</style>