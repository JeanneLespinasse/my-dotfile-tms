import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'jeanne',
      password: 'j34nn3',
      database: 'postgres',
      autoLoadEntities: true, // Automatically loads entities
      synchronize: true, // Auto-creates tables (disable in production!)
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
