import { UploadedFile } from './uploaded_file';
import { User } from './user';
import { UploadedImage } from './uploaded-image';
import { ProductFormat } from './product-format';

export interface Product {
  id: number;
  name: string;
  description: string;
  overview: string;
  highlight: string;
  theme_file: UploadedFile | null;
  owner: User;
  price: number;
  price_usd: number;
  remaining_products: number;
  thumbnail_image: UploadedImage;
  category: string;
  preview_images: UploadedImage[];
  sale_histories: number;
  author: User;
  formats: ProductFormat[];
}