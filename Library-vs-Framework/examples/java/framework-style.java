// ILLUSTRATIVE — syntax verified, not executed in CI
@RestController
class StatusController {
    @GetMapping("/status")
    Map<String, Boolean> read() { return Map.of("ok", true); }
}
