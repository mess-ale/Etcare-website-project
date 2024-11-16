<template>
    <div class="blog-image">
        <div class="blog-width space-y-4 text-primary text-justify">
            <img src="../../assets/event.png" />
            <div class="flex justify-between blog-title">
                <h1 class="text-secondary font-bold text-2xl font-oswald">Grand Appreciation and Recognition Program
                </h1>
                <h1 class="text-secondary font-bold text-2xl font-oswald">Saturday, November 23</h1>
            </div>
            <p>Join us for a day of appreciation and recognition as we celebrate outstanding achievements and honor
                remarkable individuals at the "Grand Appreciation and Recognition Program."</p>
            <ul>
                <h1>Event Details:</h1>
                <li><strong>Date:</strong> Saturday, November 23</li>
                <li><strong>Time:</strong> Starting from 9:00 AM</li>
                <li><strong>Venue:</strong> Millennium Hall</li>
            </ul>

            <p>This special program will include inspiring speeches, award presentations, and an opportunity to connect
                with like-minded individuals committed to excellence. The event is open to all who wish to be part of a
                day dedicated to celebrating hard work, success, and the spirit of achievement.
            </p>
            <p>Don’t miss this memorable occasion! Tickets are available for entry. Secure your spot and be a part of
                this remarkable gathering.</p>
        </div>
    </div>
</template>

<style>
.blog-image {
    padding: 8rem 4rem 6rem 4rem;
    justify-content: center;
    display: flex;
}

.blog-title {
    border-bottom: solid 1px theme('colors.primary');
    padding: 0.5rem 0;
}

.blog-width {
    width: 65vw;
}

.blog-image img {
    width: 65vw;
    height: 70vh;
    border-radius: 0.75rem;
}

ul li {
    padding-left: 20px;
}
</style>