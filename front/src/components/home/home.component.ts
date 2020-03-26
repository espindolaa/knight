import { Component, OnInit } from '@angular/core';
import { LocalStorageService } from 'src/services/local-storage-service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  
  public shouldShowWizard = true;
  private _localStorageManager: LocalStorageService;

  ngOnInit(): void {
    this.shouldShowWizard = this._localStorageManager.shouldShowWizard(); 
    // this.shouldShowWizard = true;
  }

  constructor(localStorageManager: LocalStorageService) {
    this._localStorageManager = localStorageManager;
  }

  public wizardShown() {
    this._localStorageManager.setShowWizard(false);
    this.shouldShowWizard = this._localStorageManager.shouldShowWizard();
  }

}
