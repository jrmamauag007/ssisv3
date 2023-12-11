//Flash Timeout
setTimeout(function() {
    // Check if the element with ID "inner-message" exists
    var innerMessage = document.getElementById("inner-message");
    // Only execute the timeout if the element exists
    if (innerMessage) {
      setTimeout(function() {
        // Apply a 2-second opacity transition
        innerMessage.style.transition = "opacity 2s";
  
        // Set the opacity to 0 (making it fade out)
        innerMessage.style.opacity = "0";
      });
    }
  }, 5000); //5 seconds to start fading
  
  // Sidebar Collapse with Ajax
  $(document).ready(function () {
    $(".navbar-toggler").click(function () {
      // Toggle the collapse class on the sidebar
      $("#sidebar").toggleClass('collapse');
  
      // Toggle the value of session.sidebar using Ajax
      $.ajax({
        type: 'GET',
        url: '/admin/toggle_sidebar',
      });
    });
  });

    // Search Script
$(document).ready(function() {
  // Listen for changes in the search input field
  $("#search-input").on("input", function() {
      var searchText = $(this).val().toLowerCase();

      // Loop through table rows and hide those that don't match the search text
      $(".highlightable-row").each(function() {
          // Get all td elements
          var tdsToSearch = $(this).find('td');

          // Concatenate the text content of each td
          var rowText = tdsToSearch.map(function() {
              return $(this).text().toLowerCase();
          }).get().join(' ');

          // Check if the rowText contains the search text
          if (rowText.indexOf(searchText) === -1) {
              $(this).hide();
          } else {
              $(this).show();
          }
      });
});
  $(".highlightable-row").each(function () {
    var status = $(this).find('td:eq(2)').text().trim().toLowerCase();
    if (status === "resolved") {
        $(this).addClass("table-secondary");
        $(this).find('td').css('font-weight', '300');
    }
});
});