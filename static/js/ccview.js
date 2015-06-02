$('#compile_btn').click(function() {
  $.ajax({
    url: '/compile',
    method: 'POST',
    data: {
      'code': $('#code_area').val(),
    },
    success: function(data, textStatus, jqXHR) {
      $('#compiler_output').val(data);
    },
  })
  return false;
});
