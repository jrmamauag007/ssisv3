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
        url: '/toggle_sidebar',
      });
    });
  });

    // Search Script for college and courses
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
});
// Search Script for students
$(document).ready(function() {
  // Listen for changes in the search input field
  $("#search-input").on("input", function() {
      var searchText = $(this).val().toLowerCase();

      // Loop through table rows and hide those that don't match the search text
      $(".highlightable-row-student").each(function() {
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
});
// Load Student Details
function loadStudentDetails(studentId) {
  // Simulate smooth transition to details page
  $("#student-details").html("Loading..."); // You can load content via AJAX

  // Navigate to details page (replace with actual URL)
  // Assuming you have a route like /student/<studentId> to handle student details
  window.location.href = `/student/${studentId}`  ;
}

// Add click event listener to highlight rows for students
$(".highlightable-row-student").click(function (event) {
  // Check if the click originated from a button inside the row
  if (!$(event.target).is('.btn')) {
    var studentId = $(this).data("id");
    loadStudentDetails(studentId);
  }
});

// Prevent button click event from propagating to the row
$(".highlightable-row-student .btn").click(function (event) {
  event.stopPropagation();
});
