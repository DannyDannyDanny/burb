module.exports = {
    devServer: {
      proxy: {
        '^/(api|uploads)': {
          target: 'http://localhost:3000',
          ws: true,
          changeOrigin: true
        }
      }
    }
  }