ns.click_rep_num = function(num){
  $('#enter_reps').val($('#enter_reps').val() + num);
}

ns.click_clear = function(){
  $('#enter_reps').val("");
}

ns.click_save = function(){
  $('#enter_reps').val();

  var data = {
    'exercise_id': $('#exercise_id').val(),
    'reps': $('#enter_reps').val()
  };

  console.log(data)

  ns.ajax({
    type: 'POST',
    url: ns.BASE_URL + '/ajax/save_set',
    data: data,
    success: function(html){
      //$('#modal').modal('hide');
      //@todo - reload the exchange list
      location.reload();
    }
  });
}