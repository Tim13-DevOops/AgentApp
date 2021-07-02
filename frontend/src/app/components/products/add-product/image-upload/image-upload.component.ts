import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ImageUploadService } from 'src/app/services/image-upload.service';

@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html',
  styleUrls: ['./image-upload.component.css']
})
export class ImageUploadComponent implements OnInit {

    // Variable to store shortLink from api response
    shortLink: string = "";
    loading: boolean = false; // Flag variable
    file: File = null; // Variable to store file

    @Output()
    imageId = new EventEmitter<string>()
  
    // Inject service 
    constructor(private fileUploadService: ImageUploadService) { }
  
    ngOnInit(): void {
    }
  
    // On file Select
    onChange(event) {
        this.file = event.target.files[0];
    }
  
    // OnClick of button Upload
    onUpload() {
        this.loading = true;
        console.log(this.file);
        this.fileUploadService.upload(this.file).subscribe(
            (name: any) => {
                this.shortLink = name;
                this.loading = false;
                this.imageId.emit(name);
            }
        , err => alert(JSON.stringify(err)));
    }

}