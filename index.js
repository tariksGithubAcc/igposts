
//Script for submiting User URL


$(document).ready(function() {
    $('#submit-url').click(function(event) {
      event.preventDefault();
      $('#loading1').show();
      $('button[id="submit-url"]').prop('disabled', true);
      var input_url = $('#id_url').val();
      console.log($('#submit-url').data('url')),
      $.ajax({
        type: 'POST',
        url: '/scrap-url/', // Replace this with the URL of your backend view
        data: {
          'url': input_url,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() // Include the CSRF token
        },
        
        success: function(response) {
          $('#loading1').hide();
        },
        error: function(response) {
          console.log(response); // Log any errors to the console
        },
        complete: function() {
              $('button[id="submit-url"]').prop('disabled', false);
              $('button[id="submit-btn"]').prop('disabled', false);
          }
      });
    });
  });
  
  
  
  
  //<!--Script for submiting User query-->
  
    $(document).ready(function() {
      $('form').submit(function(event) {
          event.preventDefault();
          $('#response').empty(); // clear previous response
          $('#loading').show();
          $('button[id="submit-btn"]').prop('disabled', true);
          $('button[id="submit-url"]').prop('disabled', true);
          $.ajax({
              type: $(this).attr('method'),
              url: '/process-form/',
              data: $(this).serialize(),
              xhrFields: {
                  withCredentials: true
              },
              success: function(response) {
                  var words = response.data.split(" ");
                  var i = 0;
                  var intervalId = setInterval(function() {
                      $('#response').append(words[i++] + " ");
                      if (i == words.length) clearInterval(intervalId);
                  }, 100);
              },
              error: function() {
                  alert('Error submitting the form!');
              },
              complete: function() {
                  $('#loading').hide();
                  $('button[id="submit-btn"]').prop('disabled', false);
                  $('button[id="submit-url"]').prop('disabled', false);
              }
          });
      });
  });
  