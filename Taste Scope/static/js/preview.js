document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.getElementById('imageInput');
    const preview = document.getElementById('preview');

    if (imageInput && preview) {
        imageInput.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            } else {
                preview.src = '#';
                preview.style.display = 'none';
            }
        });
    }

    // Initialize detail sections
    const detailSections = document.querySelectorAll('.detail-section');
    detailSections.forEach(section => section.style.display = 'none');
});

// Improved toggle logic
function toggleSection(id) {
    const sections = document.querySelectorAll('.detail-section');
    sections.forEach(section => {
        if (section.id === id) {
            section.style.display = section.style.display === 'block' ? 'none' : 'block';
        } else {
            section.style.display = 'none';
        }
    });
}
