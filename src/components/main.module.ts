import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HomeComponent } from './home/home.component';
import { LocalStorageManager } from 'src/services/local-storage-manager';
import { ChessBoardComponent } from './chess-board/chess-board.component';
import { ChessCellComponent } from './chess-cell/chess-cell.component';

@NgModule({
  declarations: [
    HomeComponent,
    ChessBoardComponent,
    ChessCellComponent
  ],
  imports: [
    BrowserModule,
  ],
  providers: [
    {
      provide: LocalStorageManager
    }
  ],
  bootstrap: [HomeComponent]
})
export class MainModule { }
