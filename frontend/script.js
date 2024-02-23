async function generateQR() {
    const url = document.getElementById('urlInput').value;
    const response = await fetch('/api/generate-qr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
});
const data = await response.json();
document.getElementById('qrCode').innerHTML = `<img src="${data.qr_code}" alt="QR Code" />`;
}