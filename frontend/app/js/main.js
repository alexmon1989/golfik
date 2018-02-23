import Vue from 'vue';
import VeeValidate, { Validator } from 'vee-validate';
import ru from 'vee-validate/dist/locale/ru';

Validator.localize('ru', ru);
Vue.use(VeeValidate, {
  locale: 'ru'
});

import ContactForm from './vue-components/ContactForm.vue';
import LoginForm from './vue-components/LoginForm.vue';
import PasswordResetForm from './vue-components/PasswordResetForm.vue';
import PasswordResetConfirmForm from './vue-components/PasswordResetConfirmForm.vue';

new Vue({
    el: '#app',
    components: {
        ContactForm: ContactForm,
        LoginForm: LoginForm,
        PasswordResetForm: PasswordResetForm,
        PasswordResetConfirmForm: PasswordResetConfirmForm,
    }
});
