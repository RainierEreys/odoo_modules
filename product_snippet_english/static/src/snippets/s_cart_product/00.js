odoo.define('product_snippet_english.product_normal_snippet', function(require) {
    'use strict';

    const widget = require('web.public.widget');

    widget.registry.normalproducts = widget.Widget.extend({
        selector: '.explore_products',
        start() {
            let products = this.el.querySelector('#products-row');
            let contacts = this.el.querySelector('#contact');

            /*SE RECIBE LA INFORMACIÓN CONSULTADA EN EL CONTROLADOR PARA ARMAR UN SNIPPET*/
            if (contacts) {
                this._rpc({
                    route: '/get_normalproducts',
                    params: {}
                }).then(data => {

                    var contactos = data['contacto'];

                    var name_contact = [];
                    var contador = [];

                    for (var i = 0; i < contactos.length; i++) {

                        name_contact.push(contactos[i].name);
                        contador.push(contactos[i].id);
                    }



                    console.log(name_contact);
                    console.log(contador);


                    console.log(contactos);

                    let html = ``
                    contactos.forEach(contacto => {
                        html += `<div class="col-lg-3 mb-5">
                            <div class="d-flex align-items-center">
                                <div class="img-container mr-3 rounded">
                                    <img class="country-image rounded img-fluid" src="data:image/png;base64,${contacto.image_1920}"/>
                                </div>
                                <div>
                                    <h5 class="mb-0">${contacto.name}</h5>
                                    <div>${contacto.email}</div>

                                </div>
                            </div>
                        </div>`
                    })
                    contacts.innerHTML = html
                })
            }

            if (products) {
                this._rpc({
                    route: '/get_normalproducts',
                    params: {}
                }).then(data => {

                    var product_data = data['product'];
                    var numero_1 = data['numero'];
                    console.log(numero_1);

                    let html = ``
                    product_data.forEach(product => {
                        html += `<div class="col-lg-3 mb-5">
                            <div class="d-flex align-items-center">
                                <div class="img-container mr-3 rounded">
                                    <img class="country-image rounded img-fluid" src="data:image/png;base64,${product.image_1920}"/>
                                </div>
                                <div>
                                <a href="${product.website_url}">
                                    <h5 class="mb-0">${product.type}</h5>
                                    <div>${product.name}</div>
                                </a>
                                </div>
                            </div>
                        </div>`
                    })
                    products.innerHTML = html

                })
            }

        },
    });
})