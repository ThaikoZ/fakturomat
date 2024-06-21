(function ($) {
  $(document).ready(function () {
    $(".tabular.inline-group").on(
      "input",
      'input[id$="-amount"], input[id$="-VAT"]',
      function () {
        var prefix = $(this).attr("id").split("-")[1];
        var amount = parseFloat($("#id_" + prefix + "-amount").val()) || 0;
        var VAT = parseFloat($("#id_" + prefix + "-VAT").val()) || 0;
        var price =
          parseFloat($("#id_" + prefix + "-product_price").val()) || 0;
        var total_price = amount * price * (1 + VAT / 100);

        $("#id_" + prefix + "-total_price").val(total_price.toFixed(2));
      }
    );
  });
})(django.jQuery);
