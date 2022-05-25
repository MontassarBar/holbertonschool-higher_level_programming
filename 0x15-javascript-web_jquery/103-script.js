$(document).ready(function () {
  const callback = function () {
    const input = document.getElementById('language_code').value;
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + input, function (data) {
      $('DIV#hello').text(data.hello);
    });
  };
  $('INPUT#language_code').keypress(function (e) {
    if (e.key === 'Enter') callback();
  });
  $('INPUT#btn_translate').click(callback);
});
