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