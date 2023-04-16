if (typeof imgPreview !== 'undefined') {
    imgPreview.onchange = evt => {
        const [file] = imgPreview.files
        if (file) {
            image.src = URL.createObjectURL(file)
        }
      }
}
