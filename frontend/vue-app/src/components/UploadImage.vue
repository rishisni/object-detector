<template>
  <div class="container">
    <br>
    <h2 class="text-center mb-4 mt-4">Upload Image</h2>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-3">
          <input type="file" @change="previewImage" class="form-control">
        </div>
        <div class="text-center mb-3">
          <button @click="uploadImage" class="btn-classic">Upload</button>
        </div>
      </div>
    </div>
    <div v-if="previewImageUrl && processedImageUrl" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <div class="d-flex justify-content-between">
          <div>
            <h3 class="text-center">Uploaded Image</h3>
            <img :src="previewImageUrl" alt="Uploaded Image" class="image">
          </div>
          <div>
            <h3 class="text-center">Processed Image</h3>
            <img :src="processedImageUrl" alt="Processed Image" class="image">
          </div>
        </div>
      </div>
    </div>
    <div v-if="carCount !== null || truckCount !== null || bikeCount !== null" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <div class="alert alert-info text-center" role="alert">
          <template v-if="carCount > 0">
            <span style="color: green;">Number of Cars Detected: {{ carCount }}</span>
            <br>
          </template>
          <template v-if="truckCount > 0">
            <span style="color: red;">Number of Trucks Detected: {{ truckCount }}</span>
            <br>
          </template>
          <template v-if="bikeCount > 0">
            <span style="color: blue;">Number of Bikes Detected: {{ bikeCount }}</span>
          </template>
        </div>
      </div>
    </div>
    <div v-if="errorMessage" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <div class="alert alert-danger text-center" role="alert">
          {{ errorMessage }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UploadImage',
  data() {
    return {
      previewImageUrl: '',
      processedImageUrl: '',
      carCount: null,
      truckCount: null,
      bikeCount: null,
      errorMessage: ''
    }
  },
  methods: {
    previewImage(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        this.previewImageUrl = reader.result;
      };
      reader.readAsDataURL(file);
    },
    uploadImage() {
      if (!this.previewImageUrl) {
        this.errorMessage = 'Please select an image.';
        return;
      }

      fetch(this.previewImageUrl)
        .then(res => res.blob())
        .then(blob => {
          const formData = new FormData();
          formData.append('file', blob, 'image.jpg');

          fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
          })
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then(data => {
            this.carCount = data.car_count;
            this.truckCount = data.truck_count;
            this.bikeCount = data.bike_count;
            this.processedImageUrl = `data:image/jpeg;base64,${data.processed_image}`;
            this.errorMessage = '';
          })
          .catch(error => {
            console.error('Error:', error);
            this.errorMessage = 'Error: Unable to connect to the server';
          });
        })
        .catch(error => {
          console.error('Error:', error);
          this.errorMessage = 'Error: Unable to process the image';
        });
    }
  }
}
</script>

<style scoped>
.image {
  max-width: 100%;
  height: auto;
}
.btn-classic {
 
  color: white; 
  background-color: black; 
  transition: all 0.3s ease; 
  border: 2px solid transparent;
  padding: 0.5rem 1rem; 
  border-radius: 0.5rem; 
  text-decoration: none;
}

.btn-classic:hover {
 
  color: black; 
  background-color: white; 
  text-decoration: none; 
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2); 
  border-color: #000; 
}
</style>
