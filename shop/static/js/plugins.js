$(document).ready(function() {
  var quantity_number = $('.q-number')

  quantity_number.bind('keyup mouseup', function(){
      $(this).parent().submit()
  })
});
