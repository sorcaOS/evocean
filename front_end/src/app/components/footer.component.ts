import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'evocean-footer',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css'
})
export class FooterComponent {

  socials = [
    {
      'image': 'assets/images/facebook.svg',
      'link': 'https://www.facebook.com/evocean/'
    },
    {
      'image': 'assets/images/instagram.svg',
      'link': 'https://www.instagram.com/evocean/'
    },
    {
      'image': 'assets/images/twitter.svg',
      'link': 'https://twitter.com/evocean/'
    },
    {
      'image': 'assets/images/github.svg',
      'link': 'https://github.com/maycuatroi/'
    }
  ];

}
