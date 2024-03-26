import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButton } from '@angular/material/button';
import { RouterLink } from '@angular/router';
import { Web3Service } from '../services/web3.service';
import { UserService } from '../services/user.service';
import { MessageService } from '@omelet/shared-components';
import { MatToolbar } from '@angular/material/toolbar';

@Component({
  selector: 'evocean-header',
  standalone: true,
  imports: [CommonModule, MatButton, RouterLink, MatToolbar],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

  constructor(
    private web3Service: Web3Service,
    private userService: UserService,
    private messageService: MessageService
  ) {

  }

  async onConnectWalletClick() {
    const publicKey = await this.web3Service.connectWeb3Wallet();
    console.log(publicKey.toString());
    this.userService.addWallet(publicKey.toString()).subscribe(
      (wallet) => {
        this.messageService.success('Wallet added successfully');
      },
      (error) => {
        this.messageService.error('Wallet add failed');
      }
    )
  }

}