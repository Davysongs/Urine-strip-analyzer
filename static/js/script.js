document.getElementById('upload-form').onsubmit = async function (e) {
    e.preventDefault();
    let formData = new FormData();
    formData.append('image', document.getElementById('image').files[0]);
    let response = await fetch('/api/upload/', {
        method: 'POST',
        body: formData
    });
    let result = await response.json();
    document.getElementById('response').innerText = JSON.stringify(result, null, 2);
}
