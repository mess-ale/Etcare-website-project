<template>
    <div>
        <ServiceCard text="Equb" imgservice="../_nuxt/assets/service/equb-p.png" />
        <div v-if="login">
            <div class="bg-secondary py-8">
                <h1 class="text-center font-bold font-oswald text-2xl">You’re Not Currently in Any Equb Group?</h1>
            </div>
            <div class="login-equb-body font-oswald py-6 text-primary grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="space-y-3">
                    <img src="../../assets/logo1-removebg.png" alt="logo" />
                    <h1 class="text-xl">Equb</h1>
                    <h1 class="text-4xl font-bold">Join or Form an Equb Group</h1>
                    <p class="font-robot text-justify text-lg">Members join or form an Equb group with peers, coworkers,
                        or
                        other SACCO members who share common
                        financial goals and trust.</p>
                    <div class="flex space-x-8">
                        <div class="equb-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2.75em" height="2.75em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M10.27 12h3.46a1.5 1.5 0 0 0 1.48-1.75l-.3-1.79a2.951 2.951 0 0 0-5.82.01l-.3 1.79c-.15.91.55 1.74 1.48 1.74m-8.61-.89c-.13.26-.18.57-.1.88c.16.69.76 1.03 1.53 1h1.95c.83 0 1.51-.58 1.51-1.29c0-.14-.03-.27-.07-.4c-.01-.03-.01-.05.01-.08c.09-.16.14-.34.14-.53c0-.31-.14-.6-.36-.82c-.03-.03-.03-.06-.02-.1c.07-.2.07-.43.01-.65a1.12 1.12 0 0 0-.99-.74a.1.1 0 0 1-.07-.03C5.03 8.14 4.72 8 4.37 8c-.3 0-.57.1-.75.26c-.03.03-.06.03-.09.02a1.24 1.24 0 0 0-1.7 1.03q0 .03-.03.06c-.29.26-.46.65-.41 1.05c.03.22.12.43.25.6c.03.02.03.06.02.09m14.58 2.54c-1.17-.52-2.61-.9-4.24-.9s-3.07.39-4.24.9A2.99 2.99 0 0 0 6 16.39V18h12v-1.61c0-1.18-.68-2.26-1.76-2.74m-15.02.93A2.01 2.01 0 0 0 0 16.43V18h4.5v-1.61c0-.83.23-1.61.63-2.29c-.37-.06-.74-.1-1.13-.1c-.99 0-1.93.21-2.78.58m21.56 0A6.95 6.95 0 0 0 20 14c-.39 0-.76.04-1.13.1c.4.68.63 1.46.63 2.29V18H24v-1.57c0-.81-.48-1.53-1.22-1.85M22 11v-.5c0-1.1-.9-2-2-2h-2c-.42 0-.65.48-.39.81l.7.63c-.19.31-.31.67-.31 1.06c0 1.1.9 2 2 2s2-.9 2-2">
                                </path>
                            </svg>

                        </div>
                        <div class="equb-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2.75em" height="2.75em" viewBox="0 0 20 20">
                                <path fill="currentColor"
                                    d="M10 6.5c-.854 0-1.617.39-2.121 1a2.75 2.75 0 0 0 1.735 4.473a5.52 5.52 0 0 1 3.136-2.689V9.25c0-.665-.236-1.275-.629-1.75c-.504-.61-1.267-1-2.121-1m8.677 4.422a5.49 5.49 0 0 0-4.932-1.87a3.7 3.7 0 0 0-.427-1.552H17.5A1.5 1.5 0 0 1 19 9v.5c0 .48-.11.964-.323 1.422M9.207 13A5.5 5.5 0 0 0 9 14.5c0 1.797.861 3.392 2.194 4.395A6.7 6.7 0 0 1 10 19c-3.14 0-5-2.029-5-4v-.5A1.496 1.496 0 0 1 6.5 13zm-4.892.284C2.205 12.713 1 11.087 1 9.5V9a1.5 1.5 0 0 1 1.5-1.5h4.183a3.7 3.7 0 0 0-.433 1.75A3.74 3.74 0 0 0 7.45 12H6.5a2.5 2.5 0 0 0-2.185 1.284M6 1a2.75 2.75 0 1 1 0 5.5A2.75 2.75 0 0 1 6 1m8 0a2.75 2.75 0 1 1 0 5.5A2.75 2.75 0 0 1 14 1m.5 18a4.5 4.5 0 1 0 0-9a4.5 4.5 0 0 0 0 9m0-7a.5.5 0 0 1 .5.5V14h1.5a.5.5 0 0 1 0 1H15v1.5a.5.5 0 0 1-1 0V15h-1.5a.5.5 0 0 1 0-1H14v-1.5a.5.5 0 0 1 .5-.5">
                                </path>
                            </svg>
                        </div>
                    </div>
                    <div class="pt-8">
                        <nuxt-link to="#equb"
                            class="equb-button transition duration-5000 ease-in-out hover:bg-secondary">
                            More Info
                        </nuxt-link>
                    </div>
                </div>

                <div class="flex items-center justify-center space-x-8">
                    <img src="../../assets/arrow-equb.png" class="items-center h-20 w-34 flex" alt="arrow equb" />

                    <nuxt-link to="#howtojoin"
                        class="equb-button transition duration-5000 ease-in-out hover:bg-secondary">
                        How to join
                    </nuxt-link>
                </div>
            </div>
        </div>

        <div v-else>
            <div class="items-cener flex justify-center space-x-16">
                <img src="../../assets/justforshow.png" />
                <div class="justify-center flex items-center">
                    <button
                        class="bg-white w-34 h-12 text-secondary font-oswald text-xl rounded-sm font-bold hover:bg-primary hover:text-white">
                        Spin
                    </button>
                </div>
            </div>

            <div class="font-robot text-primary bg-white grid grid-cols-1 md:grid-cols-2 gap-12 py-4">
                <div>
                    <div class="bg-background py-2 rounded-sm ">
                        <h1 class="font-oswald text-2xl font-bold text-center">Remaining list</h1>
                    </div>

                    <div class="flex py-2 space-x-8 items-cener justify-center shadow-md">
                            <img src="../../assets/team/PicEkram.jpg" class="w-12 h-12 equb-img" />
                            <div class="">
                                <h1 class="font-bold font-oswald">Ekram Ekram</h1>
                                <p>type: milliners</p>
                            </div>
                            <div>
                                <h1 class="font-bold font-oswald">Amount</h1>
                                <p>1,000,000 birr</p>
                        </div>
                    </div>
                </div>
                <div>
                    <div class="bg-background py-2 rounded-sm">
                        <h1 class="font-oswald text-2xl font-bold text-center">History of winners</h1>
                    </div>
                </div>
            </div>
        </div>

        <div id="equb" class="transition-all duration-500 saving-p-m flex gap-4">
            <div class="saving-left">
                <ul>
                    <h1 class="saving-title">Etcare Saccos Digital Ekub</h1>
                    <li>Digital Ekub services offered by SACCOs (Savings and Credit Cooperative Organizations) are
                        designed to modernize the traditional Ethiopian Ekub system (a group savings and lending
                        arrangement) using digital platforms. These services aim to increase accessibility, enhance
                        transparency, and streamline operations. Here's an overview of the key services typically
                        provided under digital Ekub offerings in SACCOs:
                    </li>
                </ul>

                <ul>
                    <h1 class="saving-title">Regular savings</h1>
                    <li>A member must save a minimum regular savings amount of 750.00;</li>
                    <li>Standard savings rate is based on the member's saving capacity and is based on the member's
                        application
                        It
                        must be approved by the cooperative.</li>
                    <li> Interest for the member's regular savings as determined by the cooperative's bylaws gets,
                    </li>
                </ul>


                <ul>
                    <h1 class="saving-title">Demand savings</h1>
                    <li>The amount of demand savings will be determined according to the user's capacity and
                        needs, accordingly
                        By opening a savings account starting from 500.00 Birr, saving from 100.00 Birr after the
                        account is
                        opened.</li>
                    <li>Interest for the member's savings as determined by the cooperative's bylaws It may be thought,
                        Demand savings can be spent by the member at any time;</li>
                    <li>Demand savings member can provide loan guarantee;</li>
                    <li>The member may spend interest savings only if the funds are not held as collateral;</li>
                </ul>

                <ul>
                    <h1 class="saving-title"> Time limit saving</h1>
                    <li>The minimum amount of time limit deposit will be 50 000.00/fifty thousand.</li>
                    <li>The minimum deposit period is six months.</li>
                    <li>The minimum amount of time limit deposit is 50 000.00/ fifty thousand Birr.</li>
                    <li>The deposit period is six months and the interest rate for six months is 8-12 per month The
                        amount
                        and
                        duration
                        will depend.
                        The deposit amount is more than five hundred thousand birr If it is kept for more than two
                        years,
                        the interest rate is agreed upon by the management committee It will be determined but should
                        not
                        exceed
                        13.5
                        percent. </li>
                    <li>According to the agreement that the cooperative makes with its members as necessary, for a
                        certain
                        period
                        Time
                        may accrue a non-payable time limit savings to the depositor;</li>
                    <li> Reserve the member's time limit savings for loan guarantee in the cooperative can
                    </li>
                    <li>The cooperative can encourage time saving It will be only when it is confirmed that the capacity
                        to
                        use it is high.</li>
                    <li> Time limit savings for loan guarantee until the guarantee is lifted as a cost to the member not
                        paid
                    </li>
                </ul>

                <ul>
                    <h1 class="saving-title">Interest free savings</h1>
                    <li>The cooperative is based on the member's desire and the agreement of the cooperative
                        Savings that are not
                        considered based on interest and savings for different reasons.</li>
                    <li>The right of the savings member to claim interest in any case He will not have it, but if he
                        requests to be considered for interest in the application, the interest will be granted will
                        benefit
                    </li>
                    <li>Interest-free savings can be used as loan collateral;</li>
                    <li>The member can spend the savings without considering the interest, the money as a guarantee Only
                        if
                        not caught.</li>
                </ul>

                <ul>

                    <h1 class="saving-title">Children savings</h1>
                    <li>The children of the members of the cooperative who are under 18 years of age Children you manage
                        can save children.</li>
                    <li>When children start saving, they do not pay registration or lottery fees.</li>
                    <li>The importance of having children's savings so that they have an understanding of the
                        cooperative
                        and It helps them develop a culture of saving.</li>
                    <li>The account will be opened starting with the savings amount of Birr 500.00,</li>
                    <li>Children who have been saving in the cooperative and reached the age of 18 If you meet the other
                        requirements for registration fee, you can become a member by purchasing a lot at the
                        association.
                    </li>
                    <li>Children will earn interest on their savings, but the savings interest will be added to the
                        savings.</li>
                    <li>Children's savings are used as a loan guarantee for the parents or guardians;</li>
                    <li>Children's savings account is an account that can be opened together with parents to spend
                        whenever
                        they want You can open and save a math title where you can.</li>
                </ul>

                <ul>
                    <h1 class="saving-title">Savings of women</h1>
                    <li>In order to encourage women to become entrepreneurs, it has become necessary to initiate a form
                        of
                        savings.</li>
                    <li>The importance of having women's savings so that they have an understanding of the cooperative
                        and
                        It helps them develop a culture of saving.</li>
                    <li>The account is opened starting with the savings amount of Birr 1000.00,</li>
                    <li>Women will get interest on their savings but the interest on savings will be added to the
                        savings.
                    </li>
                    <li>Women's savings are used as loan collateral;</li>
                </ul>
            </div>

            <div class="saving-right p-4">
                <div class="saving-right-box">
                    <!-- Section Header -->
                    <h1 class="text-primary font-oswald text-2xl text-center font-bold p-4">Why Save with Us?</h1>

                    <!-- Feature List -->
                    <div class="space-y-2">
                        <!-- Feature Item -->
                        <div class="flex gap-4 p-4 border-b border-gray-200">
                            <div class="flex flex-col items-center text-secondary">
                                <svg xmlns="http://www.w3.org/2000/svg" width="3.5em" height="3.5em"
                                    viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M12 19.9q2.425-.75 4.05-2.962T17.95 12H12V4.125l-6 2.25v5.175q0 .175.05.45H12zm0 2q-.175 0-.325-.025t-.3-.075Q8 20.675 6 17.638T4 11.1V6.375q0-.625.363-1.125t.937-.725l6-2.25q.35-.125.7-.125t.7.125l6 2.25q.575.225.938.725T20 6.375V11.1q0 3.5-2 6.538T12.625 21.8q-.15.05-.3.075T12 21.9">
                                    </path>
                                </svg>
                                <h2 class="text-lg font-bold mt-2">Security</h2>
                            </div>
                            <p class="text-primary items-center flex text-justify">
                                Your savings are safe with us, backed by a trusted cooperative structure.
                            </p>
                        </div>

                        <!-- Repeat for each feature -->
                        <div class="flex gap-4 p-4 border-b border-gray-200">
                            <div class="flex flex-col items-center text-secondary">
                                <svg xmlns="http://www.w3.org/2000/svg" width="3.5em" height="3.5em"
                                    viewBox="0 0 512 512">
                                    <path fill="currentColor"
                                        d="M144.938 18.063l8.437 19.187c17.36 39.43 27.86 79.965 32.563 120.313c-50.01 4.028-99.724 4.15-144.688 1.656l-21.188-1.19L33.5 174.438c42.232 51.6 93.612 82.498 148.438 110.907c-12.137 69.664-39.726 134.1-77.282 185.312L92 487.906l21.25-2.437c99.754-11.457 177.9-51.146 236.688-106.064c33.06 23.513 65.993 52.01 98.093 88.97l15.095 17.374l1.28-22.97c3.558-63.803-8.63-128.11-33.655-187.53c37.76-67.647 57.985-143.224 63.563-214.656l2-25.532l-17.97 18.22c-35.647 36.18-86.34 61.284-143.468 78.124c-46.935-47.74-104.638-85.32-170.03-106.812l-19.907-6.532z">
                                    </path>
                                </svg>
                                <h2 class="text-lg font-bold mt-2">Flexibility</h2>
                            </div>
                            <p class="text-primary text-justify">
                                Choose from various saving plans that suit your needs.
                            </p>
                        </div>

                        <div class="flex gap-4 p-4 border-b border-gray-200">
                            <div class="flex flex-col items-center text-secondary">
                                <svg xmlns="http://www.w3.org/2000/svg" width="3.5em" height="3.5em"
                                    viewBox="0 0 14 14">
                                    <path fill="currentColor" fillRule="evenodd"
                                        d="M10.326.28a.5.5 0 0 1 .506-.229l2.571.429a.5.5 0 0 1 .411.575l-.428 2.572a.5.5 0 0 1-.9.208l-.694-.97l-3.574 2.284a.75.75 0 0 1-.974-.144l-1.993-2.33L1.524 4.59a.75.75 0 1 1-.686-1.334l4.255-2.187a.75.75 0 0 1 .913.18L7.96 3.534l2.96-1.892l-.577-.807a.5.5 0 0 1-.017-.555">
                                    </path>
                                </svg>
                                <h2 class="text-lg font-bold mt-2">Growth</h2>
                            </div>
                            <p class="text-primary text-justify">
                                Earn competitive interest rates on your savings, helping you grow your funds over time.
                            </p>
                        </div>

                        <div class="flex gap-4 p-4">
                            <div class="flex flex-col items-center text-secondary">
                                <svg xmlns="http://www.w3.org/2000/svg" width="3.5em" height="3.5em"
                                    viewBox="0 0 48 48">
                                    <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="4">
                                        <path d="M42 20v19a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3h21"></path>
                                        <path d="m16 20l10 8L41 7"></path>
                                    </g>
                                </svg>
                                <h2 class="text-lg font-bold mt-2">Convenience</h2>
                            </div>
                            <p class="text-primary text-justify">
                                Manage your savings effortlessly with our user-friendly platform.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    data() {
        return {
            login: false
        }
    }
}
</script>

<style>
.login-equb-body {
    background-image: url('../../assets/car-equb.png');
    padding: 2rem 4rem;
}

.equb-img {
    border-radius: 50%;
    border: 1px solid theme('colors.secondary');
}

.equb-button {
    padding: 0.5rem 3rem;
    border-radius: 5px;
    background-color: theme('colors.primary');
    color: theme('colors.white')
}

.equb-icon {
    border: 2px solid theme('colors.secondary');
    padding: 1rem;
    border-radius: 50%;
}

.saving-p-m {
    padding: 0 4rem 6rem 4rem;
    display: flex;
}

.saving-left {
    width: 60%;
}

.saving-right {
    width: 40%;
}

.saving-right-box {
    box-shadow: 2px 2px 5px theme('colors.secondary');
    border-radius: 0.5rem;
    position: sticky;
    top: 0;
}

.saving-title {
    color: theme('colors.secondary');
    font-family: oswald, sans-serif;
    font-size: 1.5rem;
    font-weight: bold;
    padding: 1rem 0;
}

.saving-left ul li {
    color: theme('colors.primary');
    font-family: robot, sans-serif;
    padding: 5px;
}
</style>