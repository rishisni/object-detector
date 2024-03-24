<template>
  <div class="container">
    <div class="jumbotron">
      <h1 class="display-4">Welcome to Image Detector</h1>
      <p class="lead">Detect vehicles in images with ease!</p>
      <hr class="my-4">
      <p>Upload your images and let us handle the rest.</p>
      <router-link to="/upload" class="btn-classic">Upload Image</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
.btn-classic {
 
  margin-right: 1rem;
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


