
// SDK do Mercado Pago
import { MercadoPagoConfig } from 'mercadopago';
// Adicione as credenciais
const client = new MercadoPagoConfig({ accessToken: 'TEST-6850306204525311-060812-ea9d9f49e0e40a0355d0447696454c6d-305889854' });



const preference = new Preference(client);

preference.create({
  body: {
    items: [
      {
        title: 'Meu produto',
        quantity: 1,
        unit_price: 25
      }
    ],
  }
})
.then(console.log)
.catch(console.log);
