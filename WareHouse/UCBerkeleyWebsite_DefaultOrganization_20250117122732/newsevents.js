'''
This component renders the News & Events section of the UC Berkeley website.
'''
import React from 'react';
function NewsEvents() {
    return (
        <section id="news-events" aria-labelledby="news-events-heading">
            <h2 id="news-events-heading">News & Events</h2>
            <ul>
                <li>Event 1</li>
                <li>Event 2</li>
                <li>Event 3</li>
            </ul>
        </section>
    );
}
export default NewsEvents;