<template>
    <!-- Form -->
    <form class="g-py-15" @submit.prevent="login">
        <div v-if="failed" class="alert alert-danger fade show g-my-20" role="alert">
        <h4 class="h5">
            <i class="fa fa-minus-circle"></i>
            Ошибка!
          </h4>
          Неверные логин и/или пароль
        </div>

        <div :class="{'u-has-error-v1': errors.has('username') }" class="mb-4"> 
          <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Логин:</label>
          <input v-model="username" v-validate="'required'" data-vv-as="Логин" :disabled="processing" name="username" class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15" type="text" placeholder="Логин">
          <small v-show="errors.has('username')" class="form-control-feedback">{{ errors.first('username') }}</small>  
        </div>

        <div class="g-mb-35">
          <div :class="{'u-has-error-v1': errors.has('password') }" class="mb-3"> 
            <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Пароль:</label>
            <input v-model="password" v-validate="'required'" data-vv-as="Пароль" :disabled="processing" name="password" class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15" type="password" placeholder="Пароль">
            <small v-show="errors.has('password')" class="form-control-feedback">{{ errors.first('password') }}</small> 
          </div>

          <div class="row justify-content-between">
            <div class="col align-self-center">
              <label class="form-check-inline u-check g-color-gray-dark-v5 g-font-size-12 g-pl-25 mb-0">
                <input v-model="rememberme" :disabled="processing" class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" type="checkbox">
                <div class="u-check-icon-checkbox-v6 g-absolute-centered--y g-left-0">
                  <i class="fa"></i>
                </div>
                Запомнить меня
              </label>
            </div>
            <div class="col align-self-center text-right">
              <a class="g-font-size-12" href="/accounts/password_reset/">Забыли пароль?</a>
            </div>
          </div>
        </div>

        <div class="mb-4">
          <button class="btn btn-md btn-block u-btn-primary rounded g-py-13" type="submit">Вход</button>
        </div>
    </form>
    <!-- End Form -->
</template>

<script>
    import axios from '../config-axios';
    import qs from 'qs';

    export default {
        props: ['next'],
        data() {
            return {
                username: '',
                password: '',
                rememberme: false,
                processing: false,
                failed: false,
            }
        },
        methods: {
            login() {                
                this.serverErrors = [];

                this.$validator.validateAll().then(result => {
                    if (result) {
                        this.processing = true;
                        axios.post('/accounts/login/', qs.stringify({
                            username: this.username,
                            password: this.password,
                            rememberme: +this.rememberme,
                        }))
                        .then(() => {                            
                            this.failed = false;
                            this.processing = false;

                            let url = this.next ? this.next : '/';
                            window.location = url;
                        })
                        .catch(e => {
                            this.failed = true;
                            this.processing = false;
                        });
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .u-check input[type="checkbox"]:checked + .u-check-icon-checkbox-v6 i::before {
        content: '\f00c' !important;
    }
</style>