<template>
  <div>
    <form @submit.prevent="validate" id="sign-up-form" class="g-py-15" method="post" action="">
      <div v-html="csrfField"></div>

      <div class="row">
        <div class="col-xs-12 col-sm-6 mb-4">
          <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Имя:</label>
          <input class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
                 type="text"
                 v-model="first_name"
                 name="first_name"
                 placeholder="Иванов">
        </div>

        <div class="col-xs-12 col-sm-6 mb-4">
          <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Фамилия:</label>
          <input class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
                 type="text"
                 v-model="last_name"
                 name="last_name"
                 placeholder="Иван">
        </div>
      </div>

      <div :class="{'u-has-error-v1': errors.has('email') || (emailErrors.length > 0 && showServerErrors) }"
           class="mb-4">
        <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Email*:</label>
        <input class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
               type="email"
               name="email"
               v-model="email"
               @keypress="hideServerErrors()"
               v-validate="'required|email'"
               data-vv-as="Email"
               placeholder="ivanov@gmail.com">
        <small v-if="errors.has('email')" class="form-control-feedback">{{ errors.first('email') }}</small>
        <small v-if="showServerErrors && emailErrors.length > 0" class="form-control-feedback">{{ emailErrors }}</small>
      </div>

      <div :class="{'u-has-error-v1': errors.has('username') || (usernameErrors.length > 0 && showServerErrors) }"
           class="mb-4">
        <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Логин*:</label>
        <input class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
               type="text"
               name="username"
               v-model="username"
               @keypress="hideServerErrors()"
               v-validate="'required'"
               data-vv-as="Логин"
               placeholder="Логин">
        <small v-if="errors.has('username')" class="form-control-feedback">{{ errors.first('username') }}</small>
        <small v-if="showServerErrors && usernameErrors.length > 0" class="form-control-feedback">{{ usernameErrors }}
        </small>
      </div>

      <div class="row">
        <div :class="{'u-has-error-v1': errors.has('password1') || (password1Errors.length > 0 && showServerErrors) }"
             class="col-xs-12 col-sm-6 mb-4">
          <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Пароль*:</label>
          <input class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
                 type="password"
                 name="password1"
                 @keypress="hideServerErrors()"
                 v-validate="'required'"
                 data-vv-as="Пароль"
                 placeholder="Пароль">
          <small v-if="errors.has('password1')" class="form-control-feedback">{{ errors.first('password1') }}</small>
          <small v-if="showServerErrors && password1Errors.length > 0" class="form-control-feedback">{{ password1Errors
            }}
          </small>
        </div>

        <div :class="{'u-has-error-v1': errors.has('password2') || (password2Errors.length > 0 && showServerErrors) }"
             class="col-xs-12 col-sm-6 mb-4">
          <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Подтверждение пароля*:</label>
          <input class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
                 type="password"
                 name="password2"
                 @keypress="hideServerErrors()"
                 v-validate="'required'"
                 data-vv-as="Подтверждение пароля"
                 placeholder="Подтверждение пароля">
          <small v-if="errors.has('password2')" class="form-control-feedback">{{ errors.first('password2') }}</small>
          <small v-if="showServerErrors && password2Errors.length > 0" class="form-control-feedback">{{ password2Errors
            }}
          </small>
        </div>
      </div>

      <div class="row mb-5">
        <div class="col-12">
          <button class="btn btn-md btn-block u-btn-primary rounded g-py-13 g-px-25" type="submit">Зарегистрироваться
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    props: [
      'first_name',
      'last_name',
      'username',
      'email',
      'emailErrors',
      'usernameErrors',
      'password1Errors',
      'password2Errors',
      'csrfField'
    ],
    data() {
      return {
        showServerErrors: true
      }
    },
    methods: {
      hideServerErrors() {
        this.showServerErrors = false;
      },
      validate() {
        this.$validator.validateAll().then(result => {
          if (result) {
            document.getElementById("sign-up-form").submit();
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>
