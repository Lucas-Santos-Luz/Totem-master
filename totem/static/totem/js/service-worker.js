self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open('app-cache').then(function(cache) {
            return cache.addAll([
                '/',
                '/static/css/styles.css',
                '/static/js/scripts.js',
                '/static/css/modelo.css',
                '/static/js/manifest.json',
                '/static/js/service-worker.js',
                '/static/css/telaSuspensa.css',
                'totem/css/modelo.css',
                'totem/js/service-worker.js',
                'totem/js/service-worker.js',
                // Adicione outros arquivos que você deseja armazenar em cache
            ]);
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
});
