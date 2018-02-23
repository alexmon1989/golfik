<template>    
    <div>  
        <form @submit.prevent="validate" id="password-reset-confirm-form" class="g-py-15" action="" method="post">
          <div v-html="csrfField"></div>
          <div :class="{'u-has-error-v1': errors.has('new_password1') || (newpassword1Errors.length > 0 && showServerErrors) }" class="mb-4">
            <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Пароль:</label>
            <input v-model="newpassword1" 
                    @keypress="hideServerErrors()" 
                    data-vv-as="Пароль" 
                    v-validate="'required'" 
                    name="new_password1" 
                    class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15" 
                    type="password" 
                    placeholder="Пароль">
            <small v-if="errors.has('new_password1')" class="form-control-feedback">{{ errors.first('new_password1') }}</small>
            <small v-if="showServerErrors && newpassword1Errors.length > 0" class="form-control-feedback">{{ newpassword1Errors }}</small>
          </div>
          <div :class="{'u-has-error-v1': errors.has('new_password2') || (newpassword2Errors.length > 0 && showServerErrors) }" class="mb-4">           
            <label class="g-color-gray-dark-v2 g-font-weight-600 g-font-size-13">Подтверждение пароля:</label>           
            <input v-model="newpassword2" 
                    @keypress="hideServerErrors()" 
                    data-vv-as="Подтверждение пароля"
                    v-validate="'required'" 
                    name="new_password2" 
                    class="form-control g-color-black g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15" 
                    type="password" 
                    placeholder="Подтверждение пароля">
            <small v-if="errors.has('new_password2')" class="form-control-feedback">{{ errors.first('new_password2') }}</small>
            <small v-if="showServerErrors && newpassword2Errors.length > 0" class="form-control-feedback">{{ newpassword2Errors }}</small>
          </div>

          <div class="mb-4">
            <button class="btn btn-md btn-block u-btn-primary rounded g-py-13" type="submit">Сохранить</button>
          </div>
        </form>
    </div>
</template>

<script>
    export default {
        props: ['newpassword1Errors', 'newpassword2Errors', 'csrfField'],
        data() {
            return {
                newpassword1: '',
                newpassword1: '',
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
                    document.getElementById("password-reset-confirm-form").submit();
                }
            });            
          }
        }
    }
</script>

<style scoped>
  
</style>