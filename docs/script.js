let currentFeature = 1;

function showFeature(featureNumber) {
    const features = document.querySelectorAll('.feature');
    features.forEach((feature, index) => {
        feature.style.display = (index + 1 === featureNumber) ? 'block' : 'none';
    });
}

function nextFeature() {
    currentFeature = (currentFeature % 3) + 1;
    console.log(currentFeature)
    showFeature(currentFeature);
}

function previousFeature() {
    currentFeature = (currentFeature - 1) || 3;
    showFeature(currentFeature);
}

document.addEventListener('DOMContentLoaded', () => {
    showFeature(currentFeature);
});
