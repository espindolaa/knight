import { Component, OnInit } from '@angular/core';
import { LocalStorageManager } from 'src/services/local-storage-manager';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  
  title = 'knight';
  private _localStorageManager: LocalStorageManager;

  ngOnInit(): void {
  }

  constructor(localStorageManager: LocalStorageManager) {
    this._localStorageManager = localStorageManager;
  }

}
