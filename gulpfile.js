const gulp = require('gulp')
const imagemin = require('gulp-imagemin')
const clean = require('gulp-clean')
const mincss = require('gulp-cssmin')

gulp.task('copy',['clean'],()=>{
    return gulp.src('menu/static/dist/**/*')
        .pipe(gulp.dest('menu/static/assets'))
});
gulp.task('clean',()=>{
    return gulp.src('menu/static/assets')
              .pipe(clean())
});
gulp.task('build-img',['copy'],()=>{
    gulp.src('menu/static/dist/img/**/*')
      .pipe(imagemin())
      .pipe(gulp.dest('menu/static/assets/img'))
});
gulp.task('min-css',['build-img'],()=>{
  gulp.src('menu/static/dist/css/**/*.css')
      .pipe(mincss())
      .pipe(gulp.dest('menu/static/assets/css'))
});
