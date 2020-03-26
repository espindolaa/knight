import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { HomeComponent } from './home/home.component';
import { ChessService } from 'src/services/chess-service';
import { LocalStorageService } from 'src/services/local-storage-service';
import { ChessBoardComponent } from './chess-board/chess-board.component';
import { ChessCellComponent } from './chess-cell/chess-cell.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { WizardComponent } from './wizard/wizard.component';

@NgModule({
  declarations: [
    HomeComponent,
    ChessBoardComponent,
    ChessCellComponent,
    FooterComponent,
    HeaderComponent,
    WizardComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [
    {
      provide: LocalStorageService
    },
    {
      provide: ChessService
    },
    {
      provide: HttpClientModule
    }
  ],
  bootstrap: [HomeComponent]
})
export class MainModule { }
