<template>
    <div>
        <ServiceCard text="Membership Form" imgservice="../_nuxt/assets/form.jpg" />
        <div class="max-w-4xl mx-auto p-6 bg-white text-primary shadow-md rounded-md">
            <h2 class="text-2xl font-bold text-center text-secondary mb-12">EtCare Membership Form</h2>
            <form @submit.prevent="handleSubmit">
                <!-- Personal Details -->
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                    <div>
                        <label for="firstName" class="block text-sm font-medium text-primary font-bold">First Name</label>
                        <input v-model="form.firstName" id="firstName" type="text"
                            class="mt-1 p-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                            placeholder="First Name" required />
                    </div>
                    <div>
                        <label for="fatherName" class="block text-sm font-medium text-primary font-bold">Father Name</label>
                        <input v-model="form.fatherName" id="fatherName" type="text"
                            class="mt-1 p-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                            placeholder="Father Name" required />
                    </div>
                    <div>
                        <label for="grandfatherName" class="block text-sm font-medium text-primary font-bold">Grandfather
                            Name</label>
                        <input v-model="form.grandfatherName" id="grandfatherName" type="text"
                            class="mt-1 p-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                            placeholder="Grandfather Name" required />
                    </div>
                </div>

                <!-- Email -->
                <div class="mb-6">
                    <label for="email" class="block text-sm font-medium text-primary">Email Address</label>
                    <input v-model="form.email" id="email" type="email"
                        class="p-1 mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                        placeholder="Email Address" required />
                </div>

                <!-- Email -->
                <div class="mb-6">
                    <label for="phone" class="block text-sm font-medium text-primary">Phone Number</label>
                    <input v-model="form.phone" id="phone" type="tel"
                        class="p-1 mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                        placeholder="Email Address" required />
                </div>

                <!-- Saving Accounts -->
                <fieldset class="mb-6">
                    <legend class="text-sm font-medium text-primary mb-2">Saving Accounts</legend>
                    <div class="flex space-x-4">
                        <label class="flex items-center">
                            <input type="radio" value="Time deposit" v-model="form.savingAccount"
                                class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                            <span class="ml-2 text-sm">Time deposit</span>
                        </label>
                        <label class="flex items-center">
                            <input type="radio" value="Children Saving" v-model="form.savingAccount"
                                class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                            <span class="ml-2 text-sm">Children Saving</span>
                        </label>
                        <label class="flex items-center">
                            <input type="radio" value="Business Saving" v-model="form.savingAccount"
                                class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                            <span class="ml-2 text-sm">Business Saving</span>
                        </label>
                    </div>
                </fieldset>

                <!-- Loan Products -->
                <fieldset class="mb-6">
                    <legend class="text-sm font-medium text-primary mb-2">Loan Products</legend>
                    <div class="flex space-x-4">
                        <label class="flex items-center">
                            <input type="radio" value="Business Loan" v-model="form.loanProduct"
                                class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                            <span class="ml-2 text-sm">Business Loan</span>
                        </label>
                        <label class="flex items-center">
                            <input type="radio" value="Vehicle Loan" v-model="form.loanProduct"
                                class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                            <span class="ml-2 text-sm">Vehicle Loan</span>
                        </label>
                        <label class="flex items-center">
                            <input type="radio" value="Home Loan" v-model="form.loanProduct"
                                class="focus:ring-green-500 h-4 w-4 text-green-600 border-gray-300" />
                            <span class="ml-2 text-sm">Home Loan</span>
                        </label>
                    </div>
                </fieldset>

                <!-- File Upload -->
                <div class="mb-6">
                    <label for="receipt" class="block text-sm font-medium text-primary">Attach Receipt of Bank
                        Deposit:</label>
                    <input id="receipt" type="file"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500 sm:text-sm"
                        @change="handleFileUpload" />
                </div>

                <!-- Submit Button -->
                <div>
                    <button type="submit"
                        class="w-full bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2">
                        Submit
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                firstName: "",
                fatherName: "",
                grandfatherName: "",
                email: "",
                phone: "",
                savingAccount: "",
                loanProduct: "",
                receipt: null,
            },
        };
    },
    methods: {
        handleFileUpload(event) {
            this.form.receipt = event.target.files[0];
        },
        handleSubmit() {
            console.log("Form submitted:", this.form);
            alert("Form submitted successfully!");
        },
    },
};
</script>

<style>
body {
    background-color: #f9fafb;
    font-family: Arial, sans-serif;
}
</style>