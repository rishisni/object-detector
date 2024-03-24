<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <router-link to="/" class="navbar-brand">Image Detector</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/upload" class="nav-link">Upload Image</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar'
}
</script>

<style scoped>
.navbar {
  
  padding: 1rem;
}
.navbar-brand {
  
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-link {
  
  margin-right: 1rem;
  transition: all 0.3s ease; 
  border: 2px solid transparent; 
  padding: 0.5rem 1rem; 
  border-radius: 0.5rem; }

.nav-link:hover {
  
  text-decoration: none; 
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.2); 
  border-color: #fff;
}
</style>

