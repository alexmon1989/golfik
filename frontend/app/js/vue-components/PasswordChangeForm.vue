<template>
  <div>
    <form @submit.prevent="validate" id="password-change-form" class="g-py-15" action="" method="post">

      <div v-html="csrfField"></div>

      <div
        :class="{'u-has-error-v1': errors.has('old_password') || (old_passwordErrors.length > 0 && showServerErrors) }"
        class="mb-4">
        <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Старый (текущий) пароль:</label>
        <input v-model="old_password"
               @keypress="hideServerErrors()"
               data-vv-as="Старый (текущий) пароль"
               v-validate="'required'"
               name="old_password"
               class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
               type="password"
               placeholder="Старый (текущий) пароль">
        <small v-if="errors.has('old_password')"
               class="form-control-feedback">{{ errors.first('old_password') }}
        </small>
        <small v-if="showServerErrors && old_passwordErrors.length > 0"
               class="form-control-feedback">{{ old_passwordErrors }}
        </small>
      </div>

      <div
        :class="{'u-has-error-v1': errors.has('new_password1') || (new_password1Errors.length > 0 && showServerErrors) }"
        class="mb-4">
        <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Новый пароль:</label>
        <input v-model="new_password1"
               @keypress="hideServerErrors()"
               data-vv-as="Новый пароль"
               v-validate="'required'"
               name="new_password1"
               class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
               type="password"
               placeholder="Новый пароль">
        <small v-if="errors.has('new_password1')"
               class="form-control-feedback">{{ errors.first('new_password1') }}
        </small>
        <small v-if="showServerErrors && new_password1Errors.length > 0"
               class="form-control-feedback">{{ new_password1Errors }}
        </small>
      </div>

      <div
        :class="{'u-has-error-v1': errors.has('new_password2') || (new_password2Errors.length > 0 && showServerErrors) }"
        class="mb-4">
        <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Подтверждение пароля:</label>
        <input v-model="new_password2"
               @keypress="hideServerErrors()"
               data-vv-as="Подтверждение пароля"
               v-validate="'required'"
               name="new_password2"
               class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15"
               type="password"
               placeholder="Подтверждение пароля">
        <small v-if="errors.has('new_password2')"
               class="form-control-feedback">{{ errors.first('new_password2') }}
        </small>
        <small v-if="showServerErrors && new_password2Errors.length > 0"
               class="form-control-feedback">{{ new_password2Errors }}
        </small>
      </div>

      <div class="mb-4">
        <button class="btn btn-md btn-block u-btn-primary rounded g-py-13" type="submit">Сохранить</button>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: "password-change-form",
    props: ['old_passwordErrors', 'new_password1Errors', 'new_password2Errors', 'csrfField'],
    data() {
      return {
        old_password: '',
        new_password1: '',
        new_password2: '',
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
            document.getElementById("password-change-form").submit();
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>
