import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/index';
import { LoginComponent } from './login/index';

const appRoutes: Routes = [
    { path: '', component: LoginComponent },
    { path: 'results', component: HomeComponent },

    // otherwise redirect to login
    { path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoutes);