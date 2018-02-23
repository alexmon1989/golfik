<template>
  <div>
    <form @submit.prevent="validate" id="password-reset-form" class="g-py-15" action="" method="post">
      <div v-html="csrfField"></div>
      <p>Введите свой адрес электронной почты и мы вышлем вам новый пароль.</p>
      <div :class="{'u-has-error-v1': errors.has('email') || (emailServerErrors && emailServerErrors.length > 0) }"
           class="mb-4">
        <input v-model="email" @keypress="hideServerErrors()" data-vv-as="Email" v-validate="'required|email'"
               name="email"
               class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
               type="email" placeholder="johndoe@gmail.com">
        <small v-if="errors.has('email')" class="form-control-feedback">{{ errors.first('email') }}</small>
        <small v-if="showServerErrors && emailServerErrors && emailServerErrors.length > 0"
               class="form-control-feedback">{{ emailServerErrors }}
        </small>
      </div>

      <div class="mb-4">
        <button class="btn btn-md btn-block u-btn-primary rounded g-py-13" type="submit">Выслать новый пароль</button>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    props: ['emailServerErrors', 'csrfField'],
    data() {
      return {
        email: '',
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
            document.getElementById("password-reset-form").submit();
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>
