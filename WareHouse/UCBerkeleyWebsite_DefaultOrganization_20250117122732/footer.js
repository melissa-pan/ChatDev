'''
This component renders the footer section of the UC Berkeley website, including contact and privacy policy links.
'''
import React from 'react';
function Footer() {
    return (
        <footer role="contentinfo">
            <p>© 2023 UC Berkeley</p>
            <nav role="navigation" aria-label="Footer Navigation">
                <ul>
                    <li><a href="#contact" aria-label="Contact Information">Contact</a></li>
                    <li><a href="#privacy" aria-label="Privacy Policy">Privacy Policy</a></li>
                </ul>
            </nav>
        </footer>
    );
}
export default Footer;