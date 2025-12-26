// architecture-warmhouse/smart_home/services/temperature_service.go
package services

import (
 "encoding/json"
 "fmt"
 "net/http"
 "net/url" // Добавляем импорт net/url для url.QueryEscape
 "time"
)

// TemperatureService handles fetching temperature data from external API
type TemperatureService struct {
 BaseURL    string
 HTTPClient *http.Client
}

// TemperatureResponse represents the response from the temperature API
type TemperatureResponse struct {
 Value       float64   `json:"value"`
 Unit        string    `json:"unit"`
 Timestamp   time.Time `json:"timestamp"`
 Location    string    `json:"location"`
 Status      string    `json:"status"`
 SensorID    string    `json:"sensor_id"` // Имя поля соответствует Python API
 SensorType  string    `json:"sensor_type"`
 Description string    `json:"description"`
}

// NewTemperatureService creates a new temperature service
func NewTemperatureService(baseURL string) *TemperatureService {
 return &TemperatureService{
  BaseURL: baseURL,
  HTTPClient: &http.Client{
   Timeout: 10 * time.Second,
  },
 }
}

// fetchTemperature is a helper to reduce code duplication
func (s *TemperatureService) fetchTemperature(requestURL string) (*TemperatureResponse, error) {
 resp, err := s.HTTPClient.Get(requestURL)
 if err != nil {
  return nil, fmt.Errorf("error fetching temperature data from %s: %w", requestURL, err)
 }
 defer resp.Body.Close()

 if resp.StatusCode != http.StatusOK {
  // Для лучшей отладки, можно прочитать тело ошибки
  // errorBody, _ := io.ReadAll(resp.Body)
  // return nil, fmt.Errorf("unexpected status code %d from %s: %s - Body: %s", resp.StatusCode, requestURL, resp.Status, string(errorBody))
  return nil, fmt.Errorf("unexpected status code %d from %s: %s", resp.StatusCode, requestURL, resp.Status)
 }

 var temperatureResp TemperatureResponse
 if err := json.NewDecoder(resp.Body).Decode(&temperatureResp); err != nil {
  return nil, fmt.Errorf("error decoding temperature response from %s: %w", requestURL, err)
 }

 return &temperatureResp, nil
}

// GetTemperature fetches temperature data for a specific location
func (s *TemperatureService) GetTemperature(location string) (*TemperatureResponse, error) {
 // Корректно формируем URL с параметром запроса location
 url := fmt.Sprintf("%s/temperature?location=%s", s.BaseURL, url.QueryEscape(location))
 return s.fetchTemperature(url)
}

// GetTemperatureByID fetches temperature data for a specific sensor ID
func (s *TemperatureService) GetTemperatureByID(sensorID string) (*TemperatureResponse, error) {
 // Корректно формируем URL с параметром запроса sensorId
 url := fmt.Sprintf("%s/temperature?sensorId=%s", s.BaseURL, url.QueryEscape(sensorID))
 return s.fetchTemperature(url)
}
