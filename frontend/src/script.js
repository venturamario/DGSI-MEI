const videoPlayer = document.getElementById('videoPlayer');
const fileInput = document.getElementById('fileInput');

fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const fileURL = URL.createObjectURL(file);
        videoPlayer.src = fileURL;
        videoPlayer.play();
    }
});