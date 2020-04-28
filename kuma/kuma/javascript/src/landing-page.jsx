// @flow
import * as React from 'react';

import A11yNav from './a11y/a11y-nav.jsx';
import ActiveBanner from './active-banner.jsx';
import Header from './header/header.jsx';
import TaskCompletionSurvey from './task-completion-survey.jsx';
import UserProvider from './user-provider.jsx';

/**
 * This is the React component that we use for the React homepage.
 * Most of the homepage is still generated by Kuma and Jinja templates.
 * All we're doing here is rendering the page header with menus, search
 * and sign in / sign out features.
 */
export default function LandingPage() {
    return (
        <UserProvider>
            <A11yNav />
            <Header />
            <ActiveBanner />
            <TaskCompletionSurvey document={null} />
        </UserProvider>
    );
}