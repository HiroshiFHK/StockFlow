$(document).ready(function() {
    $("#searchInput").on("input", function() {
        var query = $(this).val().toLowerCase();
        $("#searchList tbody tr").each(function() {
            var rowText = $(this).text().toLowerCase();
            $(this).toggle(rowText.includes(query));
        });
    });
});