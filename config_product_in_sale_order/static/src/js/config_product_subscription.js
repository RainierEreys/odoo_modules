odoo.define("config_product_in_sale_order.config_product", function (require) {
  "use strict";
  var publicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  var ajax = require("web.ajax");
  var session = require("web.session");

  publicWidget.registry.websiteConfigProductSubscription =
    publicWidget.Widget.extend({
      selector: ".oe_website_config_product",
      events: {
        "click .check-inputs": "select_element",
        "click .create_subscription": "create_subscription",
      },
      start: function () {},
      select_element: function () {
        var container_app = document.getElementById("container_app");
        var container_invoice = document.getElementById("container_invoice");
        var contador = document.getElementById("counter_model");
        var list_product = document.getElementById("list_product");
        self.$("ul[id='list_product']").html("");
        var inputs_check = document.querySelectorAll(".check-inputs");
        var counter = 0;
        var noCheckboxSelected = true;

        inputs_check.forEach(function (input) {
          if (input.checked == true) {
            noCheckboxSelected = false;
            const imagen = document.getElementById(input.id);
            let li_list = document.createElement("li");
            li_list.className = "d-flex justify-content-between";
            const img = document.createElement("img");
            img.src = imagen.src;
            img.height = 16;
            img.className = "mr4";
            const span_name = document.createElement("span");
            span_name.textContent = input.name;
            span_name.className = "fw_semibold";
            const span_price = document.createElement("span");
            span_price.textContent = input.getAttribute("precio");
            span_price.className = "fw_semibold precio_product";
            li_list.id = input.id;
            li_list.appendChild(img);
            li_list.appendChild(span_name);
            li_list.appendChild(span_price);
            list_product.append(li_list);
            container_app.classList.remove("col-lg-10");
            container_app.classList.add("col-lg-9");
            container_invoice.classList.remove("d-none");
            counter++;
          }
        });
        if (noCheckboxSelected) {
          container_app.classList.remove("col-lg-9");
          container_app.classList.add("col-lg-10");
          container_invoice.classList.add("d-none");
        }
        contador.textContent = counter;
        var sub_total = 0;
        let total = document.querySelectorAll(".precio_product");
        total.forEach((element) => {
          var numero = parseFloat(element.innerHTML);
          sub_total += numero;
        });
        var span_total = document.getElementById("total_price");
        console.log(sub_total);
        span_total.textContent = "$ " + String(sub_total);
        console.log(String(sub_total));
      },
      create_subscription: function () {
        const ulElement = document.getElementById("list_product");
        const liElements = ulElement.getElementsByTagName("li");
        const liIds = [];
        for (const li of liElements) {
          const liId = parseFloat(li.getAttribute("id"));
          if (liId) {
            liIds.push(liId);
          }
        }
        console.log(liIds);
        return rpc
          .query({
            model: "res.users",
            method: "get_partner_id",
            args: [session.user_id],
          })
          .then(function (partner) {
            console.log(partner);
            return rpc
              .query({
                model: "sale.order",
                method: "create_sale_order_config",
                args: [partner, liIds],
              })
              .then(function (value) {
                console.log(value);
              });
          });
      },
    });
});
