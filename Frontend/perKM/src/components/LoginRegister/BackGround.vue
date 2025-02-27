<template>
    <div class="auth-container">
      <div class="stars"></div>
      <div class="content">
        <RouterView></RouterView>
      </div>
    </div>
  </template>
  
  <style scoped>
  .auth-container {
    position: relative;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(to bottom right, #000428 0%, #004e92 100%);
  }
  
  .stars {
    position: absolute;
    width: 100%;
    height: 100%;
    animation: stars-rotate 60s linear infinite;
  }
  
  .stars::after {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background-image: 
      radial-gradient(white 1%, transparent 2%),
      radial-gradient(white 1%, transparent 2%);
    background-position: 0 0, 20px 20px;
    background-size: 40px 40px;
    opacity: 0.6;
  }
  
  .content {
    position: relative;
    z-index: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }
  
  @keyframes stars-rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  </style>