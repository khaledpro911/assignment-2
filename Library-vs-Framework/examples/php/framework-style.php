// ILLUSTRATIVE — syntax verified, not executed in CI
<?php
use Symfony\Component\Routing\Attribute\Route;

final class StatusController
{
    #[Route('/status')]
    public function read(): array { return ['ok' => true]; }
}
